{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5c48e38f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import telebot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ed8a8f21",
   "metadata": {},
   "outputs": [],
   "source": [
    "TOKEN=\"6805701093:AAHkx4LAxdbeuMGAlsOrs6T1ikUzTyOfdRc\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6c609209",
   "metadata": {},
   "outputs": [],
   "source": [
    "bot = telebot.TeleBot(TOKEN)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d336ffe9",
   "metadata": {},
   "outputs": [],
   "source": [
    "@bot.message_handler(commands=['start', 'help'])\n",
    "def send_welcome(message):\n",
    "    bot.reply_to(message, \"¿Te puedo ayudar en algo?\")\n",
    "\n",
    "@bot.message_handler(func=lambda message: True)\n",
    "def echo_all(message):\n",
    "    bot.reply_to(message, message.text)\n",
    "\n",
    "bot.polling()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33bf4bb5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
