// src/components/molecules/CreatePropertyForm.jsx

import React from 'react';
import InputField from '../atoms/InputField';
import SelectField from '../atoms/SelectField';
import TextAreaField from '../atoms/TextAreaField';

const CreatePropertyForm = () => {
  const propertyTypes = [
    { label: "Casa", value: "Casa" },
    { label: "Terreno", value: "Terreno" },
    { label: "Apartamento", value: "Apartamento" },
    { label: "Edificio", value: "Edificio" },
    { label: "Local", value: "Local" },
  ];

  return (
    <section className="bg-white dark:bg-gray-900">
      <div className="max-w-2xl px-4 mx-auto">
        <form action="#">
          <div className="grid gap-4 mb-4 sm:grid-cols-2 sm:gap-6 sm:mb-5">
            <InputField label="Nombre de la propiedad" type="text" name="name" id="name" placeholder="Escriba el nombre de la propiedad" required />
            <InputField label="Dirección" type="text" name="address" id="address" placeholder="Escriba la dirección" required />
            <InputField label="País" type="text" name="pais" id="pais" placeholder="Escriba el país" required />
            <InputField label="Estado/Provincia" type="text" name="estado" id="estado" placeholder="Escriba el estado o provincia" required />
            <InputField label="Ciudad" type="text" name="ciudad" id="ciudad" placeholder="Escriba la ciudad" required />
            <InputField label="ZIP/Código Postal" type="number" name="zip" id="zip" placeholder="30107" required />
            <SelectField label="Tipo de propiedad" id="propertyType" options={propertyTypes} />
            <InputField label="Precio" type="number" name="price" id="price" placeholder="$299" required />
            <TextAreaField label="Descripción" id="descripcion" placeholder="Escriba una descripción de la propiedad..." rows={8} />
          </div>
        </form>
      </div>
    </section>
  );
};

export default CreatePropertyForm;