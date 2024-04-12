import './style.css'
import javascriptLogo from './javascript.svg'

import 'reveal.js/dist/reveal.css'
// see available themes in the
// node_modules/reveal.js/dist/theme
//  beige, black, blood, league, moon, night, serif, simple, ...
import 'reveal.js/dist/theme/sky.css'
import 'reveal.js/plugin/highlight/monokai.css'	
import Reveal from 'reveal.js'
import RevealHighlight from 'reveal.js/plugin/highlight/highlight'
import RevealMarkdown from 'reveal.js/plugin/markdown/markdown'

const deck = new Reveal()
deck.initialize({ 
  hash: true, 
  slideNumber: true,
  plugins: [ RevealHighlight, RevealMarkdown ]
})



// import { setupCounter } from './counter.js'
// document.querySelector('#app').innerHTML = `
//   <div>
//     <a href="https://vitejs.dev" target="_blank">
//       <img src="/vite.svg" class="logo" alt="Vite logo" />
//     </a>
//     <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
//       <img src="${javascriptLogo}" class="logo vanilla" alt="JavaScript logo" />
//     </a>
//     <h1>Hello Vite!</h1>
//     <div class="card">
//       <button id="counter" type="button"></button>
//     </div>
//     <p class="read-the-docs">
//       Click on the Vite logo to learn more
//     </p>
//   </div>
// `

// setupCounter(document.querySelector('#counter'))
