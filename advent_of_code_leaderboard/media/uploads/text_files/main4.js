const fs = require("fs");

function check(rap) {
  let up = true;
  let down = true;

  for (let i = 0; i < rap.length - 1; i++) {
    const d = Math.abs(rap[i] - rap[i + 1]);
    if (d < 1 || d > 3) {
      return false;
    }

    if (rap[i] < rap[i + 1]) {
      down = false;
    } else if (rap[i] > rap[i + 1]) {
      up = false;
    }
  }

  return up || down;
}

function checkWithRemove(rap) {
  for (let i = 0; i < rap.length; i++) {
    const temp = [...rap.slice(0, i), ...rap.slice(i + 1)];
    if (check(temp)) {
      return true;
    }
  }
  return false;
}

fs.readFile("input2.txt", "utf8", (err, d) => {
  if (err) {
    console.error("Erreur", err);
    return;
  }

  const r = d
    .trim()
    .split("\n")
    .map((l) => l.split(/\s+/).map(Number));
  let c = 0;

  r.forEach((rap) => {
    if (check(rap) || checkWithRemove(rap)) {
      c++;
    }
  });

  console.log(c);
});
