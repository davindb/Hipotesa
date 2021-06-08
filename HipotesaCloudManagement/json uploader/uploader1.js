const admin = require("firebase-admin");
const serviceAccount = require("./service_key.json");
// uncomment bergiliran, upload satu" jsonnya ke database
const data = require("./files/disease(1).json");
const collectionKey = "diseases";
// const data = require("./files/symptom.json");
// const collectionKey = "symptoms";
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});
const firestore = admin.firestore();
const settings = { timestampsInSnapshots: true };
firestore.settings(settings);
if (data && typeof data === "object") {
  Object.keys(data).forEach((docKey) => {
    firestore
      .collection(collectionKey)
      .doc(docKey)
      .set(data[docKey])
      .then((res) => {
        console.log("Document " + docKey + " successfully written!");
      })
      .catch((error) => {
        console.error("Error writing document: ", error);
      });
  });
}
