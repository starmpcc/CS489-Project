const express = require("express");
const router = express.Router();
const cors = require("cors");

router.get("/", cors(), (req, res) => {
  console.log("connected with server router");
  res.send({ title: "hi" });
});

module.exports = router;
