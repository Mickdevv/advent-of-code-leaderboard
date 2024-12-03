const fs = require("fs");

function isSafeReport(report) {
  let isIncreasing = true;
  let isDecreasing = true;

  for (let i = 0; i < report.length - 1; i++) {
    const diff = Math.abs(report[i] - report[i + 1]);

    if (diff < 1 || diff > 3) {
      return false;
    }

    if (report[i] < report[i + 1]) {
      isDecreasing = false;
    } else if (report[i] > report[i + 1]) {
      isIncreasing = false;
    }
  }

  return isIncreasing || isDecreasing;
}

fs.readFile("input2.txt", "utf8", (err, data) => {
  if (err) {
    console.error("Error reading file:", err);
    return;
  }

  const reports = data
    .trim()
    .split("\n")
    .map((line) => line.split(/\s+/).map(Number));

  let safeCount = 0;

  reports.forEach((report) => {
    if (isSafeReport(report)) {
      safeCount++;
    }
  });

  console.log(`Number of safe reports: ${safeCount}`);
});
