const fs = require("fs");

function calculateTotalDistance(leftList, rightList) {
  leftList.sort((a, b) => a - b);
  rightList.sort((a, b) => a - b);

  let totalDistance = 0;
  for (let i = 0; i < leftList.length; i++) {
    const distance = Math.abs(leftList[i] - rightList[i]);
    console.log(
      `Pair (${leftList[i]}, ${rightList[i]}), Distance: ${distance}`
    );
    totalDistance += distance;
  }

  console.log("Total distance calculated:", totalDistance);
  return totalDistance;
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

  calculateTotalDistance(leftList, rightList);
});
