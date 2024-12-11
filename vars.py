# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from os import environ

API_ID = int(environ.get("API_ID", "20571414"))
API_HASH = environ.get("API_HASH", "6220322f62bd4e7184c7c40afdbab304")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

txt-to-video-pdf-extractor-bot/
├── (link unavailable)
├── (link unavailable)
├── (link unavailable)
├── requirements.txt
├── (link unavailable)
└── assets/
    ├── fonts/
    │   └── OpenSans-Regular.ttf
    └── images/
        └── background.jpg


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update, ForceReply
import txt_to_video
import pdf_extractor

TOKEN = '20571414'

def start(update, context):
    context.bot.send_message(chat_id=(link unavailable), text='Welcome!')

def txt_to_video_handler(update, context):
    chat_id = (link unavailable)
    txt_file = context.bot.getFile(update.message.document.file_id)
    txt_file.download()
    video_file = txt_to_video.convert_txt_to_video(txt_file)
    context.bot.send_video(chat_id=chat_id, video=open(video_file, 'rb'))

def pdf_extractor_handler(update, context):
    chat_id = (link unavailable)
    pdf_file = context.bot.getFile(update.message.document.file_id)
    pdf_file.download()
    extracted_text = pdf_extractor.extract_text_from_pdf(pdf_file)
    context.bot.send_message(chat_id=chat_id, text=extracted_text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.document, txt_to_video_handler))
    dp.add_handler(MessageHandler(Filters.document, pdf_extractor_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


import moviepy.editor as mp
from PIL import Image, ImageDraw, ImageFont

def convert_txt_to_video(txt_file):
    # Create a video from the text
    video = mp.VideoFileClip('background.mp4')
    text_clip = mp.TextClip(txt_file, fontsize=70, color='white')
    video = mp.CompositeVideoClip([video, text_clip])
    video.write_videofile('output.mp4')
    return 'output.mp4'


import PyPDF2

def extract_text_from_pdf(pdf_file):
    # Extract text from the PDF
    pdf = PyPDF2.PdfFileReader(pdf_file)
    text = ''
    for page in range(pdf.numPages):
        text += pdf.getPage(page).extractText()
    return text

pip install python-telegram-bot
moviepy
Pillow
PyPDF2


