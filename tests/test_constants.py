import pytest
from pykakasi import kakasi

from src.constants import (
    HIRAGANA_BASE,
    DAKUON,
    COMBO,
    SMALL_っ,
    LONG_VOWEL,
    HIRAGANA
)

@pytest.fixture
def kks():
    """Fixture to provide a configured kakasi instance"""
    kks = kakasi()
    kks.setMode("H", "a")
    return kks

def verify_romanization(kks, japanese, expected):
    """Helper function to verify romanization using pykakasi"""
    result = kks.convert(japanese)
    assert result[0]['hepburn'] == expected.lower(), \
        f"Incorrect romanization for {japanese}. Expected {expected}, got {result[0]['hepburn']}"

@pytest.mark.parametrize("hiragana,romaji", HIRAGANA_BASE.items())
def test_base_hiragana(kks, hiragana, romaji):
    """Test all base hiragana characters"""
    verify_romanization(kks, hiragana, romaji)

@pytest.mark.parametrize("hiragana,romaji", DAKUON.items())
def test_dakuon(kks, hiragana, romaji):
    """Test all dakuon characters"""
    verify_romanization(kks, hiragana, romaji)

@pytest.mark.parametrize("hiragana,romaji", COMBO.items())
def test_combo(kks, hiragana, romaji):
    """Test all combination characters"""
    verify_romanization(kks, hiragana, romaji)

@pytest.mark.parametrize("hiragana,romaji", [
    ("っか", "kka"),
    ("っさ", "ssa"),
    ("った", "tta"),
    ("っぱ", "ppa")
])
def test_small_tsu(kks, hiragana, romaji):
    """Test small tsu combinations"""
    verify_romanization(kks, hiragana, romaji)

@pytest.mark.parametrize("hiragana,romaji", LONG_VOWEL.items())
def test_long_vowel(kks, hiragana, romaji):
    """Test long vowel combinations"""
    verify_romanization(kks, hiragana, romaji)

@pytest.mark.parametrize("hiragana,romaji", HIRAGANA.items())
def test_combined_hiragana(kks, hiragana, romaji):
    """Test that all dictionaries are properly combined"""
    verify_romanization(kks, hiragana, romaji) 