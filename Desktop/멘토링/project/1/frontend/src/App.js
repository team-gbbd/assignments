import React, { useState, useEffect } from "react";

function App() {
  const [count, setCount] = useState(0);

  // (처음 한 번) 현재 카운트 불러오기
  useEffect(() => {
    fetch("http://localhost:5000/count/get")
      .then(res => res.json())
      .then(data => setCount(data.count));
  }, []);

  // 증가 버튼 클릭
  const handleIncrement = () => {
    fetch("http://localhost:5000/count/increment", { method: "POST" })
      .then(res => res.json())
      .then(data => setCount(data.count));
  };

  // 감소 버튼 클릭
  const handleDecrement = () => {
    fetch("http://localhost:5000/count/decrement", { method: "POST" })
      .then(res => res.json())
      .then(data => setCount(data.count));
  };

  return (
    <div style={{ textAlign: "center", marginTop: 50 }}>
      <h1>카운트: {count}</h1>
      <button onClick={handleDecrement}>- 감소</button>
      <button onClick={handleIncrement}>+ 증가</button>
    </div>
  );
}

export default App;