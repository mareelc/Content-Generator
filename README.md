
<h2>Content Generator</h2>
A Python microservice that takes 2 keywords as input and generates a paragraph from Wikipedia. The first keyword 
determines the article, and the paragraph contains both keywords. Can be run from the command line with 
an input.csv file contianing keywords, or from a GUI where keywords can be entered and output displayed. 
Output is automatically written to output.csv. 
<br>
Content Generator is also compatible to communicate with a Life Generator microservice via the 
multiprocessing module in Python. 
<br>
<br>
<h3>Generate a Paragraph Via GUI:</h3>
<br>
<img src="https://github.com/heinl11/Content-Generator/blob/main/Content-Generator.gif" />
<br>
<br>
<h3>GUI Error Handling:</h3>
<ul>
  <li>No more than 1 word per keyword.</li>
  <li>First keyword must be valid article.</li>
  <li>Paragraph with both keywords not found.</li>
  <li>If disambiguation page, select preferred article.</li>
</ul>
<br>
<img src="https://github.com/heinl11/Content-Generator/blob/main/Content-Generator-Errors.gif" />

