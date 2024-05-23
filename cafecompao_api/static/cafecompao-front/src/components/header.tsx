'use client'

import { useState } from 'react'
import "bootstrap-icons/font/bootstrap-icons.css";
import Link from 'next/link'
// import { useUser } from '../lib/hooks' // Assuming you have a hook to get user data

export default function Header() {
  // const user = useUser();

  return (
    <header>
      <nav>
        <span className="logo">
          <i className="bi bi-cup-hot"></i>
          Café com Pão
        </span>
        <ul>
          <li><Link href="/">Principal</Link></li>
          <li><Link href="/padarias">Padarias</Link></li>
          <li><Link href="/cestas">Cestas</Link></li>
          <li><Link href="/sobre">Sobre</Link></li>
        </ul>
        <Link href="/login" className="btn btn-primary">Entrar</Link>
        {/* {user && user.isAuthenticated ? (
                    <Link href="/minha_conta" className="btn btn-primary"><i className="bi bi-house"></i> Minha Conta</Link>
                ) : (
                    <Link href="/login" className="btn btn-primary">Entrar</Link>
                )} */}
      </nav>
    </header>
  )
}