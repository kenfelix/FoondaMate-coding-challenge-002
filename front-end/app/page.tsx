"use client"

import Image from 'next/image'
import { Inter } from 'next/font/google'
import styles from './page.module.css'
import foondamatelogo from '../public/foondamatelogo.webp'
import { useEffect, useState } from 'react'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  const register = () => {
    fetch('http://127.0.0.1:8000/user')
  }

  const login = () => {

    const opts = {
      method: 'POST',
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: JSON.stringify({
        "username": email,
        "password": password,
      })
    }

    fetch('http://127.0.0.1:8000/login/', opts)
      .then(resp => {
        if (resp.status === 200) return resp.json();
        else alert("Invalid credentials")
      })
      .then()
      .catch(error => {
        console.error("something went wrong", error)
      })
  }
  // useEffect(() => {
  //   fetch()
  // })
  return (
    <div className='p-[20px] flex flex-col items-center space-y-24'>
      <div className='flex flex-row justify-between items-center space-x-[7rem]'>
        <Image src={foondamatelogo} alt={'logo'} className='h-[50px] w-[120px]' />
        <form className='flex flex-row justify-between items-center space-x-3'>
          <input type="email" placeholder='test@email.com' value={email} onChange={(e) => setEmail(e.target.value)} className='bg-slate-300 border-1 border-solid border-purple-600 rounded-[16px] py-2 px-4' />
          <input type="password" placeholder='********' value={password} onChange={(e) => setPassword(e.target.value)} className='bg-slate-300 border-1 border-solid border-purple-600 rounded-[16px] py-2 px-4' />
          <input type="submit" value="Register" onClick={register} className='bg-purple-600 rounded-[16px] py-2 px-4 text-white cursor-pointer' />
          <input type="submit" value="Login" onClick={login} className='bg-purple-600 rounded-[16px] py-2 px-4 text-white cursor-pointer' />
        </form>
      </div>
      <div>
        <form className='flex flex-row justify-between items-center space-x-3'>
          <input type="text" placeholder='input equation (e.g 7x-2=21 or 2(4x + 3)+3=24-4x)' className='bg-slate-300 border-1 border-solid border-purple-600 rounded-[16px] py-2 px-4' />
          <input type="submit" value="Solve" className='bg-purple-600 rounded-[16px] py-2 px-4 text-white cursor-pointer' />
        </form>
      </div>
    </div>
  )
}
