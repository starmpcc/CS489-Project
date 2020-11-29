const express = require("express");
const router = express.Router();
const cors = require("cors");
const { PythonShell } = require("python-shell");

router.get("/", (req, res) => {
  console.log("get request");
  res.send({ title: "Now Reo..." });
});

module.exports = router;
