
////good grief it's working now as of 3:58 PST august 14, remember you have to let it read and view channels. This is a config issue not a code one

require('dotenv').config();

const Discord = require('discord.js');


// const { Client, GatewayIntentBits } = require('discord.js');
///const client = new Client({ intents: [GatewayIntentBits.Guilds] });

const client = new Discord.Client();
///https://stackoverflow.com/questions/69201388/client-missing-intents
// const client = new Client({ intents: ["GUILDS", "GUILD_MESSAGES"], ws: {intents: ["GUILDS", "GUILD_MESSAGES"]} });


client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);

});



// resources used
//https://forum.freecodecamp.org/t/node-js-discord-bot-client-missing-intents/478271
//https://stackoverflow.com/questions/68694195/how-do-i-fix-client-missing-intents-error ?
///https://discordjs.guide/popular-topics/intents.html#enabling-intents


client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('pong');
    console.log("info")
  }
});

client.login(process.env.DISCORD_TOKEN);