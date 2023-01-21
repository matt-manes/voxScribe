import time
from pathlib import Path

import pytest

from voxscribe import voxscribe

MP3_url = (
    "https://github.com/matt-manes/voxscribeTestAudio/blob/main/testaudio.mp3?raw=true"
)
WAV_url = (
    "https://github.com/matt-manes/voxscribeTestAudio/blob/main/testaudio.wav?raw=true"
)
local_WAV = Path(__file__).parent / "testaudio.wav"
local_MP3 = Path(__file__).parent / "testaudio.mp3"
local_MP3_2 = Path(__file__).parent / "testaudio2.mp3"


def test_voxscribe_download_audio_file():
    filepath = voxscribe.download_audio_file(MP3_url, ".mp3")
    assert filepath.exists()


def test_voxscribe_convert_MP3_to_WAV():
    WAVpath = voxscribe.convert_MP3_to_WAV(local_MP3_2)
    assert WAVpath.exists()
    assert WAVpath.with_suffix(".mp3") == local_MP3_2
    WAVpath.unlink()


def test_voxscribe_get_text_from_url():
    assert voxscribe.get_text_from_url(MP3_url, ".mp3") == "hell does exist"
    assert voxscribe.get_text_from_url(WAV_url, ".wav") == "hell does exist"


def test_voxscribe_get_text_from_WAV():
    assert voxscribe.get_text_from_WAV(local_WAV) == "hell does exist"


def test_voxscribe_get_text_from_MP3():
    assert voxscribe.get_text_from_MP3(local_MP3) == "hell does exist"


def test_voxscribe_clean_up():
    audiopath = Path(__file__).parent.parent / "src" / "voxscribe" / "audio"
    audiopath.mkdir(exist_ok=True)
    (audiopath / "dummy.file").touch()
    time.sleep(1)
    voxscribe.clean_up(0)
    assert len(list(audiopath.iterdir())) == 0
