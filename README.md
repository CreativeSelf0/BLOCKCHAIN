# Simple Blockchain 
This project helped to get a glimpse of Satoshi Nakamoto Idea of Blockchain.

The white paper Link: [https://bitcoin.org/bitcoin.pdf] 

In addition to this link: [https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/].

It went step by step explaining the python code above and the white paper idea.
I also added a post method so you can mine a new blockchain. 

# How to install:
1 - Install the files.

2 - run the blockchain python script 
  ```
  python blockchain.py
  ```
3 - go to 127.0.0.1:5000/chain in your browser

4 - if you want to create a new block:
  ```
  curl -X POST -H "Content-Type: application/json" -d ' {"dummy data": 521 , "dumb": 1000} ' http://localhost:5000/chain
  ```
  
  
5 - Refresh the page and you will get the new mined block.


Enjoy =) !


