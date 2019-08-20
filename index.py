#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Score import Score

score = Score()

print("Content-type: text/html; charset=utf-8\n")


html = """<!DOCTYPE html>
<link href="style/main.css" rel="stylesheet" type="text/css">
<script type="text/javascript" src="/js/jquery-3.4.1.min.js"></script>
<head>
    <title>2048</title>
</head>
<body>
    <div class="intro">
        <h1 class="title">2048</h1>
        <div class="scores-container">
            Score
            <div class="score-container">0</div>
            Meilleur
            <div class="best-container">{0}</div>
        </div>
    </div>
    <div class="game-container">
        <div class="grid-container">
            <div class="grid-row">
                <div class="grid-cell" id="tile1"></div>
                <div class="grid-cell" id="tile2"></div>
                <div class="grid-cell" id="tile3"></div>
                <div class="grid-cell" id="tile4"></div>
            </div>
            <div class="grid-row">
                <div class="grid-cell" id="tile5"></div>
                <div class="grid-cell" id="tile6"></div>
                <div class="grid-cell" id="tile7"></div>
                <div class="grid-cell" id="tile8"></div>
            </div>
            <div class="grid-row">
                <div class="grid-cell" id="tile9"></div>
                <div class="grid-cell" id="tile10"></div>
                <div class="grid-cell" id="tile11"></div>
                <div class="grid-cell" id="tile12"></div>
            </div>
            <div class="grid-row">
                <div class="grid-cell" id="tile13"></div>
                <div class="grid-cell" id="tile14"></div>
                <div class="grid-cell" id="tile15"></div>
                <div class="grid-cell" id="tile16"></div>
            </div>
        </div>
    </div> 
    <div class="debugger">
        <div class="currentFunction">
        </div>
        <div class="details">
        </div>
    </div>
    <script type="text/javascript" src="/js/script.js"></script>
</body>
</html>
""".format(score.high)

print(html)