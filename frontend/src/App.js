import React, { useState } from "react";
import Editor from "react-simple-code-editor";
import Prism from "prismjs";
import "prismjs/themes/prism.css";
import "prismjs/components/prism-python";
import "prismjs/components/prism-c";
import "prismjs/components/prism-javascript";

function App() {
  const [code, setCode] = useState("print('Hello from Python!')");
  const [output, setOutput] = useState("");
  const [lang, setLang] = useState("python");

  const handleCodeChange = (newCode) => setCode(newCode);

  const runCode = async () => {
    try {
      const res = await fetch("http://localhost:5000/execute", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code, lang }),
      });
      const data = await res.json();
      setOutput(data.result);
    } catch (err) {
      setOutput("Error: " + (err.message || err));
    }
  };

  const outputLines = output.split("\n");

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h2>Code Editor</h2>

      <select
        value={lang}
        onChange={(e) => setLang(e.target.value)}
        style={{ marginBottom: 12, padding: 4 }}
      >
        <option value="python">Python</option>
        <option value="c">C</option>
        <option value="javascript">JavaScript</option>
      </select>

      <Editor
        value={code}
        onValueChange={handleCodeChange}
        highlight={(c) => Prism.highlight(c, Prism.languages[lang], lang)}
        padding={10}
        style={{
          fontFamily: '"Fira code", "Fira Mono", monospace',
          fontSize: 14,
          minHeight: "200px",
          border: "1px solid #ccc",
          borderRadius: "4px",
          backgroundColor: "#ffffff",
          color: "#000000",
        }}
      />

      <div style={{ marginTop: 12 }}>
        <button onClick={runCode} style={{ marginRight: 10, padding: "8px 16px", cursor: "pointer" }}>
          Run
        </button>
        <button
          onClick={() => { setCode(""); setOutput(""); }}
          style={{ padding: "8px 16px", cursor: "pointer" }}
        >
          Clear
        </button>
      </div>

      <h3 style={{ marginTop: 18 }}>Output:</h3>
      <div
        style={{
          backgroundColor: "#1e1e1e",
          padding: 12,
          borderRadius: 4,
          minHeight: 120,
          fontFamily: '"Fira code", monospace',
          whiteSpace: "pre-wrap",
        }}
      >
        {outputLines.map((line, index) => {
          const isErrorLine = /(Traceback|Error|Exception|SyntaxError)/.test(line);
          return (
            <div key={index} style={{ color: isErrorLine ? "red" : "#00ff00" }}>
              {line}
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default App;
