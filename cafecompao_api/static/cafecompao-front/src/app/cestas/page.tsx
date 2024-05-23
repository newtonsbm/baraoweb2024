'use client'

import { useEffect, useState } from 'react'

export default function Padarias() {
  const [cestaList, setCestaList] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/cestas/")
      .then(response => {
        console.log(response)
        return response.json();
      })
      .then(data => setCestaList(data))
      .catch(error => console.error(error));
  }, []);

  return (
    <>
      <div id="hero" style={{ backgroundImage: "url(/images/cafepaoHero.png)" }}>
        <hgroup>
          <h1>Cestas para todos gostos!</h1>
        </hgroup>
      </div>

      <section className="container card-container">
      {cestaList.map((cesta, index) => (
        <a href={`/cestas_detail/${cesta.id}`} className="card" key={cesta.id} >
          <img src={cesta.imagem} alt="cesta" />
          <div className="card-detail">
            <h3>{cesta.nome}</h3>
            <p>{cesta.descricao}</p>
            <span className="preco">{cesta.preco}</span>
          </div>
        </a>

      ))}
      </section>
    </>
  );
}