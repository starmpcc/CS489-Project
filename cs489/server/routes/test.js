const express = require("express");
const router = express.Router();
const cors = require("cors");
var { PythonShell } = require("python-shell");

router.get("/", (req, res) => {
  console.log("test for review score");
  res.send({ title: "hi for coming to test" });
});

async function using_bert(sentence) {
  var options = { args: [content] };
  PythonShell.run(
    "/Users/songminjae/Desktop/cs489-Project/bert/infer.py",
    options,
    function (err, results) {
      if (err) throw err;
      console.log("ssss", results);
      score = results;
    }
  );
}

router.get("/:id", async (req, res) => {
  let content = req.params.id;
  console.log("fixed score of:", content);
  //////////////////////////////////////////////////////////
  let score = 0;
  var options = {
    args: [content],
  };
  PythonShell.run(
    "/Users/songminjae/Desktop/CS489-Project/bert/infer.py",
    options,
    function (err, results) {
      if (err) throw err;
      console.log("ssss", results);
      score = results;
      res.send({ score: score });
    }
  );
  ///////////////////////////////////////////////////////////
});

module.exports = router;
