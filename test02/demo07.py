# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
html_doc="""
<div class="yylFl div1">
  超级大乐透
</div>
<div class="yylFl div2" style="width:300px;">
  每周一、三、六开奖
</div>
<div class="yylFl div3">
  <span>
    <a href="#">最近30期</a>
  </span><span>
    <a style="color:#cd1d27;" href="#">最近50期</a>
  </span><span>
    <a href="#">最近100期</a>
  </span>
</div>
"""
soup=BeautifulSoup(html_doc,"html.parser")
print(soup.a)