#!/usr/bin/env python3

from sys import argv, stdin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
  options = Options()
  options.add_argument("--headless")
  driver = webdriver.Chrome(options=options)

  help = """
  cat urls.txt | ./ssweb.py
  -- or --
  python3 ssweb.py {file path}
  """

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

  for url in urls:
    imageName = url.replace('.', '_').replace(':', '_').replace('/', '').strip() + ".png"
    driver.get(url)
    driver.save_screenshot(imageName)
  driver.quit()

if __name__=="__main__":
  main()
