import redis from 'redis';

const client = redis.createClient();
// client.on('error', (err) => { console.log('Error ' + err); }); // error handler
client.on('error', (error) => console.error(`Redis client not connected to the server: ${error.message}`));
client.on('connect', () => console.log('Redis client connected to the server'));

const KEY = 'HolbertonSchools'; // key to store the list of schools in Redis

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, index) => { // store the list of schools in Redis
  client.hset(KEY, key, values[index], redis.print);
});

client.hgetall(KEY, (err, value) => { // print the list of schools stored in Redis
  console.log(value);
});
