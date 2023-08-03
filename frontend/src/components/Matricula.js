export function Matricula({ matricula }) {
    return (
        <div className="h-12 bg-[#1c1c1c] text-white flex items-center justify-center rounded-md hover:bg-gray-500 hover:scale-100 hover:h-14 transition-all">
            <p>{matricula}</p>
        </div>
    )
        
}