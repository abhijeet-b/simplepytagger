from urllib.request import urlretrieve
from mutagen.id3 import ID3, APIC, TALB, TDRC, TIT2, TRCK
from mutagen import File
import mutagen
import glob

def apply_album_art(mp3_file: str, url: str):
    if url.split('.')[-1] == 'jpg' or 'jpeg':
        urlretrieve(url, 'thumbnail.jpg')
    else:
        res_ = input('Are you sure this is a .jpg or .jpeg file? ')
        if res_.lower() == 'yes' or 'y':
            urlretrieve(url, 'thumbnail.jpg')
        else:
            return
    song = ID3(mp3_file)
    with open('thumbnail.jpg', 'rb') as cover:
        song['APIC'] = APIC(
            encoding=3,
            mime='image/jpeg',
            type=3,
            desc=u'Cover',
            data=cover.read()
        )
    song.save()


def apply_album_title(mp3_file: str, name: str):
    song = ID3(mp3_file)
    song["TALB"] = TALB(text=name)
    song.save()


def apply_release_year(mp3_file: str, year: str):
    song = ID3(mp3_file)
    song["TDRC"] = TDRC(text=year)
    song.save()


def apply_track_title(mp3_file: str, name: str):
    song = ID3(mp3_file)
    song["TIT2"] = TIT2(text=name)
    song.save()


def apply_track_idx(mp3_file: str, idx: str):
    song = ID3(mp3_file)
    song["TRCK"] = TRCK(text=idx)
    song.save()


if __name__ == "__main__":
    apply_album_title('doth')
    apply_album_art('https://f4.bcbits.com/img/a1184758497_10.jpg')
    apply_release_year('1996')
    apply_track_idx('file_example_MP3_700KB.mp3', '2')
    apply_track_title('file_example_MP3_700KB.mp3', 'creme')

