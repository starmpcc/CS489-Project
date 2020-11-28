const express = require("express");
const router = express.Router();
const cors = require("cors");

router.get("/", (req, res) => {
  console.log("get request");
  res.send({ title: "안녕하세요" });
});

module.exports = router;
