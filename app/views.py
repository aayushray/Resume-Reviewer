import PyPDF2

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ResumeForm
from .utils import generate_feedback
# from .pdf_parser import extract_text_from_pdf

def extract_text_from_pdf(file):
    text = ""
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text += page.extract_text()

    return text


def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume_text = extract_text_from_pdf(resume.resume_file)
            feedback = generate_feedback(resume_text)
            resume.save()
            return render(request, 'app/feedback.html', {'feedback': feedback, 'resume_text': resume_text})
    else:
        form = ResumeForm()
    return render(request, 'app/upload.html', {'form': form})
