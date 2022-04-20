var i = 2;

function timedCount() {
  i = i ** 2;
  postMessage(i);
  setTimeout("timedCount()",3000);
}

timedCount();