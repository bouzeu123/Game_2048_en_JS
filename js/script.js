$(document).ready(function(){
  intiGrid();
  document.addEventListener("keydown",eventHandler)
  score = 0; // variable globale
});

/***********************************************************/

/*
penser a utiliser forEach sur les éléments de tableaux
voir aussi for ... in
*/

function randomInt(min, max){
 return Math.floor(Math.random() * (max - min + 1)) + min;
}

function tileColor(value){
    let colors = {0: '#848484', 2: '#FFF700', 4: '#FFFF6B', 8: '#FF7F00',
                 16: '#D6710C', 32: '#B9260A', 64: '#ED0000', 128: '#FFD700',
                256: '#FFD700', 512: '#FFD700', 1024: '#FFD700', 2048: '#FFD700',
               4096: '#FFD700', 8192: '#FFD700', 16384: '#FFD700', 32786: '#FFD700'};
    return colors[value];
}

function getRandomTile(){
    let tileNumber = randomInt(1,16);
    return $('#tile'+tileNumber.toString());
}

function getRandomTileValue(){
    let values = Array(2,2,2,2,2,2,2,2,2,4);
    return values[randomInt(0,10)];
}

function value(tile){
    let parsed = parseInt(tile.text(),10);
  if (isNaN(parsed)) { return 0 }
  return parsed;
}

function setValue(tile, newValue){
    if(newValue != 0 && newValue != undefined)   tile.text(newValue.toString());
    else                                         tile.text("");
    tile.css("background-color", tileColor(newValue));
}

function addScore(value){
    score += value;
    $('.score-container').text(score.toString());
    if(highScore()<score){
        $('.best-container').text(score.toString());
    }
}

function highScore(){
    let valueStr = $('.best-container').text();
    let value = parseInt(valueStr,10);
    if (isNaN(value)) { return 0 }
  return value;
}

function addNewTile(){
    let tile = getRandomTile();
    while(value(tile) != 0)
        tile = getRandomTile();
    setValue(tile,getRandomTileValue());
}

function intiGrid(){
    addNewTile();
    addNewTile();
}

function eventHandler(event) {
    const left = 37;
    const up = 38;
    const right = 39;
    const down = 40;
    
    switch (event.keyCode) {
        case left: moveLeft(); break;
        case right: moveRight(); break;
        case up: moveUp(); break;
        case down: moveDown(); break;
    }
}

function getGridValues(){
    let matrix = [];
    for(let i=0; i<4; i++) {
        matrix[i] = [];
        for(let j=0; j<4; j++)
            matrix[i][j] = value( $('#tile'+String(4*i+j+1) ) );
    }
    return matrix;
}

function extend(array,extention){
    for(let i=0; i<extention; i++)
        array.push(0);
    return array;
}

function merge(row){
    let store = [];
    let result = [];
    // suppression des zéros inutiles
    for(let i=0; i<4; i++) {
        if(row[i] === undefined) row[i] = 0;
        if(row[i] !== 0) store.push(row[i]);
    }
    extend(store,row.length - store.length);
    let i = 0;
    while(i < store.length - 1){
        if(store[i] === store[i + 1]){
            let colapse = store[i] + store[i + 1];
            result.push(colapse);
            addScore(colapse);
            i += 2;
        }
        else {
            result.push(store[i]);
            i += 1;
        }
    }
    result.push(store[store.length-1]);  // ajout du dernier élément
    extend(result,row.length - result.length);
    return result;
}

function setGridValues(matrix){
    for(let i=0; i<4; i++) {
        for(let j=0; j<4; j++) {
            let tileNumber = 4 * i + j + 1;
            let tile = $('#tile' + tileNumber.toString());
            setValue(tile, matrix[i][j]);
        }
    }
}

function move(matrix){
    if(isGameOver()){
        if(isWin()) alert("Bravo! Vous avez gagné!");
        else        alert("Perdu! Vous avez seulement réalisé "+maxInGameBoard()+" quel résultat minable!");
    }
    else {
        for (let i = 0; i < 4; i++) {
            matrix[i] = merge(matrix[i]);
        }
    }
    return matrix;
}

function moveLeft(){
    let matrix = move(getGridValues());
    setGridValues(matrix);
    if(!gameBoardIsFull()){
        addNewTile();
    }
}

function moveRight(){
    let matrix = mirror(getGridValues());
    matrix = move(matrix);
    setGridValues(mirror(matrix));
    if(!gameBoardIsFull()){
        addNewTile();
    }
}

function moveUp(){
    let matrix = transpose(getGridValues());
    matrix = move(matrix);
    setGridValues(transpose(matrix));
    if(!gameBoardIsFull()){
        addNewTile();
    }
}

function moveDown(){
    let matrix = antitranspose(getGridValues());
    matrix = move(matrix);
    setGridValues(antitranspose(matrix));
    if(!gameBoardIsFull()){
        addNewTile();
    }
}

function mirror(matrix){
    matrix.forEach((row)=> row.reverse());
    return matrix;
}

function transpose(matrix){
    let store = [];
    for(let i=0; i<4; i++) {
        store[i] = [];
        for(let j=0; j<4; j++)
            store[i][j] = matrix[j][i];
    }
    return store;
}

function antitranspose(matrix){
    let store = [];
    length = matrix.length;
    for(let i=0; i<4; i++) {
        store[i] = [];
        for(let j=0; j<4; j++)
            store[i][j] = matrix[length-1-j][length-1-i];
    }
    return store;
}

function gameBoardIsFull(){
    let matrix = getGridValues();
    for(let i=0; i<4; i++){
        for(let j=0; j<4; j++){
            if(matrix[i][j] === 0)  return false;
        }
    }
    return true;
}

function gameBoardIsNotMovable(){
    let matrix = getGridValues();
    for(let i=0; i<4; i++) {
        for(let j=0; j<4; j++)
            if (matrix[i][j] === matrix[i][j + 1]) return false;
    }
    matrix = transpose(matrix);
    for(let i=0; i<4; i++) {
        for(let j=0; j<4; j++)
            if (matrix[i][j] === matrix[i][j + 1]) return false;
    }
    return true;
}

function isGameOver(){
    return gameBoardIsFull() && gameBoardIsNotMovable();
}

function debbug(func,data){
    $('.currentFunction').text(func);
    if(data != undefined) {
        $('.details').text(data);
    }
}

function maxInGameBoard(){
    let matrix = getGridValues();
    let maxInRows = [];
    for(let i=0; i<4; i++){
        maxInRows[i] = Math.max(...matrix[i]);
    }
    return Math.max(...maxInRows);
}

function isWin(){
    return maxInGameBoard() > 2048;
}