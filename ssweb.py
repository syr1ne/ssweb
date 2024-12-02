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
    input_stream = stdin                                     
  else:
    try:
      input_filename = argv[1]
      input_stream = open(input_filename, 'r')
    except IndexError:
      print(help)
      exit()

  for line in input_stream:
    print(line)

  # with open(args.file, 'r') as file:
  #   for url in file:
  #     print(url)
  #     driver.get($url)
  #     driver.save_screenshot("test.png")
  #   driver.quit()

if __name__=="__main__":
  main()
