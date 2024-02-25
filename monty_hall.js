
const nodePath = process.argv[0];
const appPath = process.argv[1];

const gamerType = process.argv[2] ? process.argv[2] : 'looser';
const gamesAmount = process.argv[3] ? process.argv[3] : 100;
const doorsAmount = process.argv[4] ? process.argv[4] : 3;

// Create empty doors pool and place automobile behind the one door
function getDoors(doorsAmount) {
    let doors = {};
    for (let i = 1; i <= doorsAmount; i++) {
        doors[i] = {
            'automobile': false,
            'open': false
        }
    }

    const doorAutomobile = Math.floor(Math.random() * doorsAmount) + 1;
    doors[doorAutomobile]['automobile'] = true

    return doors;
}

// Open the doors so that 2 remain closed
function openDoors(doors, choice) {
    let doorsOpen = 0;
    for (const door in doors) {
        if (doorsOpen === doorsAmount - 2) break;
        if (door === choice) continue;
        if (doors[door]['automobile']) continue;
        doors[door]['open'] = true;
        doorsOpen++;
    }
    return doors;
}


// choice other closed door
function changechoice(doors, choice) {
    for (const door in doors) {
        if (!doors[door]['open'] && door !== choice) {
            choice = door;
            break;
        }
    }
    return choice;
}

// Game
function game() {
    let wins = 0;
    let losses = 0;

    for (let i = 0; i < gamesAmount; i++) {
        let doors = getDoors(doorsAmount);
        let choice = Math.floor(Math.random() * doorsAmount) + 1;
        doors = openDoors(doors, choice);

        if (gamerType == 'perfect') choice = changechoice(doors, choice);

        doors[choice]['automobile'] ? wins++ : losses++;
    }
    return { wins, losses };
}


const { wins, losses } = game();
const winsPercent = Math.floor(wins / gamesAmount * 100, 2)
const lossesPercent = Math.floor(losses / gamesAmount * 100, 2)

console.log('----- MONTY HALL GAME ---');
console.log(`gamer type: ${gamerType}\ngames amount: ${gamesAmount}\ndoors amount: ${doorsAmount}`);
console.log(`wins: ${winsPercent}%\nlosses: ${lossesPercent}%`);
console.log('-------------------------');