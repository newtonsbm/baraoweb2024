'use client'

import { useEffect, useState } from 'react'

interface Padaria {
  id: number;
  nome: string;
  imagem: string;
  endereco: {
    cidade: string;
    rua: string;
  }
}


export default function Padarias() {
  const [padariaList, setPadariaList] = useState<Padaria[]>([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/padarias/")
      .then(response => {
        console.log(response)
        return response.json();
      })
      .then(data => setPadariaList(data))
      .then(() => console.log(padariaList))
      .catch(error => console.error(error));
  }, []);

  return (
    <>
      <div id="hero" style={{ backgroundImage: "url(/images/cafepaoHero.png)" }}>
        <hgroup>
          <h1>Conheça nossas Padarias!</h1>
        </hgroup>
      </div>

      {padariaList.map((padaria, index) => (
        <section key={padaria.id} className="featured container">
          <img src={padaria.imagem} alt="padaria" />
          <div>
            <h2>{padaria.nome}</h2>
            <ul>
              <li>Endereço: {padaria.endereco.cidade}</li>
              <li>Telefone: {padaria.endereco.rua}</li>
            </ul>
          </div>
          {index !== padariaList.length - 1 && <hr />}
        </section>
      ))}

    </>
  )
}