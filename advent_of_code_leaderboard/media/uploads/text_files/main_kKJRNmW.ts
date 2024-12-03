

function readInput(){
  const input = Deno.readTextFileSync("./input.txt")
  return input;
}

function parseReports(input: string){
  const reports: int[][] = [];
  for (const line of input.split("\n")) {

    const stringLevels = line.split(" ");

    const levels = stringLevels.map((levelString) => parseInt(levelString)).filter((level) => !isNaN(level));

    reports.push(levels);
}

  return reports;
}

function isReportSafe(report: int[]){
    if(!report.length) return false;
    let order = 0;
    let prev = report[0];

    let safe = true;

    for(let i = 1; i < report.length; i++){
        const level = report[i];

        if(order === 0 ){
            if(level < prev) order = -1;
            else if(level > prev) order = 1;
        }

        if((order === -1 && level > prev) || (order === 1 && level < prev)) {
            safe = false;
            break;
        }

        const levelDiff = Math.abs(level - prev);
        if(levelDiff > 3 || levelDiff < 1){
            safe = false;
            break;
        }

        prev = level;
    }

    return safe;
}


function isReportSafeWithDampener(report: int[]){
   let safe = isReportSafe(report);

   if(!safe){  
        for(let i = 0; i <= report.length - 1; i++){
            const modifiedReport = report.slice(0, i).concat(report.slice(i + 1));
            safe = isReportSafe(modifiedReport);
            if(safe) break;
        }
   }
   

    return safe;
}

function part1(){
  const input = readInput();

  const reports = parseReports(input);

  const safeReports = reports.filter(report => isReportSafe(report))
  
  console.warn('Safe reports: ',safeReports.length);
  
}

function part2(){
    const input = readInput();

    const reports = parseReports(input);
    
    const safeReports = reports.filter(report => isReportSafeWithDampener(report))
  
    console.warn('Safe reports with dampener: ',safeReports.length);
}

part1();

part2();