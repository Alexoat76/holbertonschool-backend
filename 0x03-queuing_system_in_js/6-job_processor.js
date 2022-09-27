import kue from 'kue';
// Create a queue named 'push_notification_code' using kue to send push notifications
const queue = kue.createQueue();

function sendNotification (phoneNumber, message) {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
}

const queueName = 'push_notification_code';

queue.process(queueName, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
