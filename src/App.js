import './App.css';
import ReactDOM from 'react-dom';
import React from 'react'

let Inode = 7;

function Test(){
  return <h1 className="hola" act="hola" onClick={Create}>Hola alex</h1>
}

function Create() {
  Inode = Inode + 10;
  const v1 = () => {
    return <h3 style={{position: "absolute", top: Inode, left: "0"}}>Hola Mundo!!!</h3>
  }
} 

function App() {
  return (
    <div className="App">
      <header id="App-header" className="App-header">
        <h1 className="hola" act="hola">Hola alex</h1>
      </header>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Create />);
root.render(<Test />);

export default App;
