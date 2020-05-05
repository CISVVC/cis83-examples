#!/usr/bin/env python3


def capitalize_sentence(s):
   
   sentences = s.split('. ')
   new_sentences = ""
   for s2 in sentences:
      new_sentences += s2.capitalize() + '. '
   
   return new_sentences



print(capitalize_sentence("this is a sentence. this is also a sentence."))


