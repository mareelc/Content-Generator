<h4>Laura Maree</h4>
<h5>2.12.2021
<h4>Content Generator</h4>

To run on Command Line (windows):
<ol>
<li>Navigate to directory with content_generator.py on command line.</li>
<li>Install wikipedia module by typing: pip install wikipedia.</li>
<li>To run without an input csv: 
<ul>Type: python content_generator.py</ul>
<ul>Hit enter and the GUI will open and you can enter 2 keywords to find a wikipedia article (from keyword 1) 
that includes a paragraph that contains both keywords.</ul>
<ul>Press the "generate" button to generate output.</ul>
<ul>Popups may occur if an error is found.</ul>
<ul>Paragraph will appear in the output textbox on the right.</ul>
<ul>The output is automatically saved to output.csv (located in the same directory).</ul>
</li>
<li>To run with an input.csv file:
<ul>Include an input.csv file in the same directory with appropriate format.</ul> 
<ul>Type: python content_generator.py input.csv</ul>
<ul>Hit enter and the program will run and search for the paragraph.</ul>
<ul>The GUI will not open.</ul>
<ul>The output (paragraph or error message) will be saved to output.csv in the same directory.</ul>
</li></ol>
