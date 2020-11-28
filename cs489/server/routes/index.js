const express = require("express");
const router = express.Router();
const cors = require("cors");
const { PythonShell } = require("python-shell");

router.get("/", (req, res) => {
  console.log("get request");
  res.send({ title: "Now Reo..." });
});

router.get("/test", (req, res) => {
  console.log("test for review score");
});

module.exports = router;
