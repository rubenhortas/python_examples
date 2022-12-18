#!/usr/bin/env python3
from stegano import lsb

MESSAGE = 'https://www.youtube.com/watch?v=QH2-TGUlwu4'
ORIGINAL_IMAGE = 'nyancat.png'
IMAGE_WITH_SECRET_MESSGAE = 'nyan_with_secret.png'


def hide_message():
    try:
        # Hide a message (string) in an image with the LSB technique.
        secret = lsb.hide(ORIGINAL_IMAGE, MESSAGE)

        # Save the image with the hidden message
        secret.save(IMAGE_WITH_SECRET_MESSGAE)

        print('Secret hidden!')
    except Exception as e:
        print(e)


def find_message():
    try:
        # Find the message in the image (with the LSB technique).
        print(f'Our secret is: {lsb.reveal(IMAGE_WITH_SECRET_MESSGAE)}!')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    hide_message()
    find_message()
