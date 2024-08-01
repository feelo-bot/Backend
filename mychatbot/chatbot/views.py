from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import random
import os

def load_data_from_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')

@api_view(['GET'])
def get_question(request):
    file_path = r'C:\Users\vnfma\Desktop\새싹톤\Chatbot\response_6.csv'
    try:
        data = load_data_from_csv(file_path)
    except FileNotFoundError:
        return Response({"error": "File not found"}, status=404)
    
    question_number = random.randint(0, len(data) - 1)
    item = data[question_number]
    
    choices = [item['answer'], item['wrong1'], item['wrong2']]
    random.shuffle(choices)
    
    return Response({
        "situation": item['situation'],
        "choices": choices,
        "answer": item['answer'],
        "hint": item['hint'],
        "similar": [item['similar1'], item['similar2'], item['similar3']]
    })