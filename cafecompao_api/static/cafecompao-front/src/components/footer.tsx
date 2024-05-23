import Image from 'next/image'
import { Facebook, Instagram, Pinterest, CupHotFill} from 'react-bootstrap-icons'

export default function Footer() {
    return (
        <footer>
            <span className="logo">
                <i className="bi bi-cup-hot"></i>
                CAFÉ COM PÃO
            </span>
            <hr />
            <div id="social">
                <a href="https://www.facebook.com/" target="_blank" rel="noreferrer">
                    <Facebook color="black" size={32} />
                </a>
                <a href="https://www.instagram.com/" target="_blank" rel="noreferrer">
                    <Instagram color="black" size={32} />
                </a>
                <a href="https://www.pinterest.com/" target="_blank" rel="noreferrer">
                    <Pinterest color="black" size={32} />
                </a>
            </div>
        </footer>
    )
}