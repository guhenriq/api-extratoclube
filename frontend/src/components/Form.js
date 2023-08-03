import { useState } from "react"
import { mask, unMask } from "node-masker"
import { FaSearch } from "react-icons/fa"
import { api } from "../service/service"
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { Results } from "./Results";

export function Form() {

    const [cpf, setCPF] = useState("")
    const [data, setData] = useState({})

    const buscarMatriculas = async (e) => {
        e.preventDefault()

        try {
            if (cpf === '') throw new Error("Necessário preecher o cpf! ")
    
            const response = await api.get(`/consultar-matricula/${mask(cpf, "999.999.999-99")}`)

            if (response.data.msg) {
                toast.info(response.data.msg)
            } else {
                setData(response.data)
            }
        } catch(err) {
            console.log(err.message)
            toast.error(err.message)
        }
    }

    return (
        <>
            <form className="w-full flex justify-center mt-36 gap-3" >
                <ToastContainer />
                <input 
                    className="lg:w-4/12 h-10 rounded-md p-3 placeholder:p-3 focus:outline-none" 
                    type="text" 
                    placeholder="Digite o número do cpf"
                    onChange={({ target }) => {
                        setCPF(unMask(target.value))
                    }}
                    value={mask(cpf, "999.999.999-99")}
                />
                <button className="bg-red-700 px-4 rounded-md text-white hover:bg-red-400 transition-all" type="submit" onClick={buscarMatriculas}>
                    <FaSearch/>
                </button>
            </form>
            <Results data={data}/>
        </>
    )
}