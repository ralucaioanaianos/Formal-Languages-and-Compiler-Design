package ro.ubb.lab11.web.converter;


import org.springframework.stereotype.Component;
import ro.ubb.lab11.core.model.Airplane;
import ro.ubb.lab11.web.dto.AirplaneDTO;

@Component
public class AirplaneConverter extends BaseConverter<Long, Airplane, AirplaneDTO> {
    @Override
    public Airplane convertDtoToModel(AirplaneDTO dto) {
        var model = new Airplane();
        model.setId(dto.getId());
        model.setModel(dto.getModel());
        model.setCapacity(dto.getCapacity());
        model.setRegistration(dto.getRegistration());
        model.setFabricationYear(dto.getFabricationYear());

        return model;
    }

    @Override
    public AirplaneDTO convertModelToDto(Airplane airplane) {
        var dto = new AirplaneDTO(airplane.getModel(), airplane.getCapacity(), airplane.getRegistration(), airplane.getFabricationYear());
        dto.setId(airplane.getId());
        return dto;
    }
}
