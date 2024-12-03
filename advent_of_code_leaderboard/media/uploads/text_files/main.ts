
function readInput(){
  const input = Deno.readTextFileSync("./input.txt")
  return input;
}


function parseLists(input: string){
  const leftList = [], rightList = [];

  for (const line of input.split("\n")) {
    const [left, right] = line.split("   ");

    const parsedLeft = parseInt(left);
    const parsedRight = parseInt(right);

    if(!isNaN(parsedLeft)) leftList.push(parsedLeft);
    if(!isNaN(parsedRight)) rightList.push(parsedRight);
  }

  return [leftList, rightList];
}

function part1(){
  const input = readInput();

  const [leftList, rightList] = parseLists(input);
  
  leftList.sort((a, b) => a - b);
  rightList.sort((a, b) => a - b);

  let totalDistance = 0;

  for (let i = 0; i < leftList.length; i++) {
    totalDistance+= Math.abs(leftList[i] - rightList[i]);  
  }

  console.warn('Total Distance: ',totalDistance);
  
}

function part2(){
  const input = readInput();

  const [leftList, rightList] = parseLists(input);
  
  const rightMap = new Map<number, number>();

  for (let i = 0; i < rightList.length; i++) {
    rightMap.set(rightList[i], (rightMap.get(rightList[i]) ?? 0) + 1);
  }

  let similarityScore = 0;
  
  for (let i = 0; i < leftList.length; i++) {
    similarityScore += leftList[i] * (rightMap.get(leftList[i]) ?? 0)
  }

  console.warn('Similarity Score: ',similarityScore);
}

part1();

part2();