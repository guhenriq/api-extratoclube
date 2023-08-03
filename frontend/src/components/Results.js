import { Matricula } from "./Matricula"

export function Results({ data }) {
    return (
        <div className="w-full flex justify-center mt-6">
            <div className="lg:w-[37.5%] gap-4 flex flex-col">
                {data.matriculas ? (
                    data.matriculas.map((matricula, idx) => {
                    return <Matricula matricula={matricula} key={idx}/>
                    })
                ) : ('') 
                }
            </div>
        </div>
    )
}