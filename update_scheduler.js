import { MongoClient } from "mongodb";
import { URI, db, arrivalDepartureCollection } from './config.json';

const uri = URI;

const client = new MongoClient(uri);

async function run() {
    try {
        const database = client.db(db);
        const collection = database.collection(arrivalDepartureCollection);

        const query = {
            'date': new Date().getDate(),
            'arrived': true,
            'departured': false
        };
        const updateDocument = {
            $set: {
                "presence_duration": {
                    $function:
                    {
                        body: function (enter_exit_time) {
                            let sum = 0;
                            if (enter_exit_time.length % 2 != 0) {
                                enter_exit_time.push(new Date())
                            }
                            for (let i = 0; i < enter_exit_time.length - 1; i++) {
                                if (i % 2 == 0) {
                                    sum += Math.abs(arr[i] - arr[i + 1]);
                                }
                            }
                            return sum
                        },
                        args: ["$enter_exit_time"],
                        lang: "js"
                    }
                }
            }
        };
        const movie = await collection.updateMany(query, updateDocument);

        console.log(movie);
    } finally {
        await client.close();
    }
}
run();