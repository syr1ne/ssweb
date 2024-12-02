#!/usr/bin/env python3

import os
from sys import argv, stdin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

help = """
for single page ss:
  echo "https://site.com" | ./ssweb.py
for list of url ss:
  cat urls.txt | ./ssweb.py
  -- or --
  ./ssweb.py {file path}
"""

def main():
  options = Options()
  options.add_argument("--headless")
  driver = webdriver.Chrome(options=options)

  if not stdin.isatty():
    urls = stdin                                     
  else:
    try:
      file = argv[1]
      try:
        urls = open(file, 'r')
      except FileNotFoundError:
        print("file doesn't exist!")
        exit()

    except IndexError:
      print(help)
      exit()

  ss_dir = os.path.join(os.getcwd(), "screenshots")
  os.makedirs(ss_dir, exist_ok=True)

  for url in urls:

    image_name = url.replace('.', '_').replace(':', '_').replace('/', '').strip() + ".png"
    driver.get(url)
    image_path = os.path.join(ss_dir, image_name)
    driver.save_screenshot(image_path)
  driver.quit()

if __name__=="__main__":
  main()
