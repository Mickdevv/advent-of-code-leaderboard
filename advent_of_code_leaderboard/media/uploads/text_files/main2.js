const fs = require("fs");

function calculateSimilarityScore(leftList, rightList) {
  const rightListCount = rightList.reduce((acc, number) => {
    acc[number] = (acc[number] || 0) + 1;
    return acc;
  }, {});

  let totalScore = 0;

  for (let i = 0; i < leftList.length; i++) {
    const leftNumber = leftList[i];
    const countInRightList = rightListCount[leftNumber] || 0;
    totalScore += leftNumber * countInRightList;
    console.log(
      `Number ${leftNumber} appears ${countInRightList} times in the right list, adding ${
        leftNumber * countInRightList
      } to the score.`
    );
  }

  console.log("Total similarity score calculated:", totalScore);
  return totalScore;
}

fs.readFile("input.txt", "utf8", (err, data) => {
  if (err) {
    console.error("Error reading file:", err);
    return;
  }

  const lines = data.trim().split("\n");
  const nombres = lines.flatMap((row) => row.trim().split(/\s+/).map(Number));

  const leftList = [];
  const rightList = [];

  nombres.forEach((value, index) => {
    if (index % 2 === 0) {
      leftList.push(value);
    } else {
      rightList.push(value);
    }
  });

  calculateSimilarityScore(leftList, rightList);
});
