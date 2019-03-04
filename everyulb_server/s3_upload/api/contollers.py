# Author: Chirag Chamoli
# -*- coding: utf-8 -*-


from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view
from django.http import HttpResponse, Http404

from ..models import Upload
from .serializer import UploadSerializer

import boto3
import environ
from urllib.parse import quote_plus
import os

# PUBLIC S3 URL: https://github.com/CollectionFS/Meteor-CollectionFS/issues/832#issuecomment-151525893

# FILE PUBLIC: https://stackoverflow.com/questions/41904806/how-to-upload-a-file-to-s3-and-make-it-public-using-boto3

class UploadFileS3(APIView):
    parser_classes = (MultiPartParser, )

    def get(self, request, format=None):
        uploads = Upload.objects.all()
        serializer = UploadSerializer(uploads, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        env = environ.Env()
        environ.Env.read_env()

        ACCESS_KEY_ID = env('ACCESS_KEY_ID')
        SECRET_ACCESS_KEY = env('SECRET_ACCESS_KEY')
        REGION_NAME = env('REGION_NAME')
        BUCKET_NAME = env('BUCKET_NAME')

        s3 = boto3.client('s3',
                          aws_access_key_id=ACCESS_KEY_ID,
                          aws_secret_access_key=SECRET_ACCESS_KEY,
                          region_name=REGION_NAME)


        file_obj = request.FILES['file']
        filename = request.FILES['file'].name

        Key = filename

        files = s3.list_objects(Bucket=BUCKET_NAME)['Contents']
        for file in files:
            if filename in file['Key']:
                return Response({"Error" : "Filename already present"})

        s3.upload_fileobj(file_obj, BUCKET_NAME, filename, ExtraArgs={'ACL':'private'})

        object_details = s3.head_object(Bucket=BUCKET_NAME, Key=Key)

        public_url = f"https://s3-{quote_plus(REGION_NAME)}.amazonaws.com/{quote_plus(BUCKET_NAME)}/{quote_plus(Key)}"

        title, extension = os.path.splitext(filename)
        
        data = {}
        data['name'] = filename
        data['extension'] = extension
        data['title'] = title
        data['mimeType'] = object_details['ContentType']
        data['webLink'] = public_url
        data['filePath'] = Key
        data['size'] = object_details['ContentLength']
        serializer = UploadSerializer(data=data)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveDestroyFileS3(APIView):

    def get(self, request, id, format=None):
        upload = Upload.objects.get(id=id)
        serializer = UploadSerializer(upload)
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        upload = Upload.objects.get(id=id)
        serializer = UploadSerializer(upload)

        env = environ.Env()
        environ.Env.read_env()

        ACCESS_KEY_ID = env('ACCESS_KEY_ID')
        SECRET_ACCESS_KEY = env('SECRET_ACCESS_KEY')
        REGION_NAME = env('REGION_NAME')
        BUCKET_NAME = env('BUCKET_NAME')

        s3 = boto3.client('s3',
                          aws_access_key_id=ACCESS_KEY_ID,
                          aws_secret_access_key=SECRET_ACCESS_KEY,
                          region_name=REGION_NAME)

        s3.delete_object(Bucket=BUCKET_NAME, Key=serializer.data['filePath'])

        upload.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def force_download(request, id, format=None):
    upload = Upload.objects.get(id=id)
    serializer = UploadSerializer(upload)

    env = environ.Env()
    environ.Env.read_env()

    ACCESS_KEY_ID = env('ACCESS_KEY_ID')
    SECRET_ACCESS_KEY = env('SECRET_ACCESS_KEY')
    REGION_NAME = env('REGION_NAME')
    BUCKET_NAME = env('BUCKET_NAME')


    s3 = boto3.client('s3',
                      aws_access_key_id=ACCESS_KEY_ID,
                      aws_secret_access_key=SECRET_ACCESS_KEY,
                      region_name=REGION_NAME)

    Key = serializer.data['filePath']

    file = s3.get_object(Bucket=BUCKET_NAME, Key=Key)

    response = HttpResponse(file['Body'].read(), content_type=file['ContentType'])
    response['Content-Disposition'] = f'attachment; filename=\"{Key}\"'
    return response

@api_view(['GET'])
def set_file_status(request, id, format=None):
    upload = Upload.objects.get(id=id)
    serializer = UploadSerializer(upload)

    para = request.GET.get('status')

    env = environ.Env()
    environ.Env.read_env()

    ACCESS_KEY_ID = env('ACCESS_KEY_ID')
    SECRET_ACCESS_KEY = env('SECRET_ACCESS_KEY')
    REGION_NAME = env('REGION_NAME')
    BUCKET_NAME = env('BUCKET_NAME')

    s3 = boto3.client('s3',
                      aws_access_key_id=ACCESS_KEY_ID,
                      aws_secret_access_key=SECRET_ACCESS_KEY,
                      region_name=REGION_NAME)

    Key = serializer.data['filePath']
    if not para or para.lower() != 'public':
        set_status = s3.put_object_acl(Bucket=BUCKET_NAME, Key=Key, ACL='private')
    else:
        set_status = s3.put_object_acl(Bucket=BUCKET_NAME, Key=Key, ACL='public-read')

    tt = s3.get_object_acl(Bucket=BUCKET_NAME, Key=Key)

    return Response(tt, status=status.HTTP_202_ACCEPTED)
