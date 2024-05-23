import Image from "next/image";
import styles from "./page.module.css";
import "bootstrap/dist/css/bootstrap.min.css";

export default function Home() {
  return (
    <main>
      <div id="hero" style={{ backgroundImage: "url(/images/cafepaoHero.png)" }}>
        <hgroup>
          <h1>Assine sua manhã perfeita!</h1>
          <p>
            Comece suas manhãs com sabor e praticidade Assine o Café com Pão!
          </p>
        </hgroup>
      </div>

      <section className="featured container">
        <Image src="/images/breadsHome.png" alt="cesta com paes" 
          width={0}
          height={0}
          sizes="100vw"
          style={{ width: '100%', height: 'auto' }} 
          />
        <div>
          <h2>Cestas com produtos perfeitos!</h2>
          <p>
            Nosso compromisso com a qualidade e a conveniência torna cada entrega uma experiência única. Experimente o que temos a oferecer
          </p>
          <ul>
            <li>Variedade Premium</li>
            <li>Personalização Flexível</li>
            <li>Entrega Confiável</li>
          </ul>
        </div>
      </section>

      <section className="quote">
        <blockquote className="container">
          Adoro receber minha cesta de café da manhã do Café com Pão toda semana! A variedade de itens frescos e a qualidade dos produtos superam minhas expectativas. Começo cada manhã com um sorriso graças a essa delícia. Recomendo a todos que buscam praticidade e sabor na primeira refeição do dia!
          <br />
          <cite>— Maria da Silva, São Paulo</cite>
        </blockquote>
      </section>
    </main>
  );
}