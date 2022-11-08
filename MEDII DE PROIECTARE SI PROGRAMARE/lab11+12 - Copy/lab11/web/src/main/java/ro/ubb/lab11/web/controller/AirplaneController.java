package ro.ubb.lab11.web.controller;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ro.ubb.lab11.core.model.Airplane;
import ro.ubb.lab11.core.service.IAirplaneService;
import ro.ubb.lab11.web.converter.AirplaneConverter;
import ro.ubb.lab11.web.dto.AirplaneDTO;
import ro.ubb.lab11.web.dto.AirplanesDTO;

import java.util.ArrayList;
import java.util.List;

@RestController
public class AirplaneController {
    public static final Logger logger = LoggerFactory.getLogger(AirplaneController.class);

    @Autowired
    private IAirplaneService airplaneService;
    @Autowired
    AirplaneConverter airplaneConverter;
    /*@Autowired
    private IPetService petService;*/

    @RequestMapping(value = "/airplanes", method = RequestMethod.GET)
    AirplanesDTO getAllAirplanes() {
        logger.warn("getAllAirplanes: ");
        List<Airplane> airplanes = airplaneService.getAllAirplanes();
        AirplanesDTO AirplanesDTO = new AirplanesDTO(airplaneConverter.convertModelsToDTOs(airplanes));
        logger.trace("Airplanes: " + AirplanesDTO);
        return AirplanesDTO;
    }

    @RequestMapping(value = "/airplanes", method = RequestMethod.POST)
    AirplaneDTO addAirplane(@RequestBody AirplaneDTO airplaneDTO) {
        logger.trace("addAirplane - AirplaneDTO: " + airplaneDTO);
        var airplane = airplaneConverter.convertDtoToModel(airplaneDTO);
        var result = airplaneService.addAirplane(airplane.getModel(), airplane.getCapacity(), airplane.getRegistration(), airplane.getFabricationYear());
        var resultModel = airplaneConverter.convertModelToDto(result);
        logger.trace("addAirplane - Airplane added");
        return resultModel;
    }

    @RequestMapping(value = "/airplanes/{id}", method = RequestMethod.PUT)
    AirplaneDTO updateAirplane(@PathVariable Long id, @RequestBody AirplaneDTO airplaneDTO) {
        logger.trace("updateAirplane - AirplaneDTO: " + airplaneDTO);
        var airplane = airplaneConverter.convertDtoToModel(airplaneDTO);
        var result = airplaneService.updateAirplane(id, airplane.getModel(), airplane.getCapacity(), airplane.getRegistration(), airplane.getFabricationYear());
        var resultModel = airplaneConverter.convertModelToDto(result);
        logger.trace("updateAirplane - airplane updated");
        return resultModel;
    }

    @RequestMapping(value = "/airplanes/filter/{name}")
    AirplanesDTO findAirplaneByName(@PathVariable String model) {
        logger.trace("findAirplaneByModel - model = {}", model);
        List<Airplane> airplanes = airplaneService.findAirplanesByModel(model);
        AirplanesDTO airplanesDTO = new AirplanesDTO(airplaneConverter.convertModelsToDTOs(airplanes));
        logger.trace("getAllAirplanes: " + airplanes);
        return airplanesDTO;
    }

    @RequestMapping(value = "/airplanes/{id}", method = RequestMethod.DELETE)
    ResponseEntity<?> deleteAirplane(@PathVariable Long id) {
        airplaneService.deleteAirplane(id);
        return new ResponseEntity<>(HttpStatus.OK);
    }

    @RequestMapping(value = "/airplanes/sort", method = RequestMethod.GET)
    AirplanesDTO getAirplanesSortedByName() {
        List<Airplane> airplanes = airplaneService.findAllByOrderByAgeAsc();
        AirplanesDTO dtos = new AirplanesDTO(airplaneConverter.convertModelsToDTOs(airplanes));
        return dtos;

    }

    //@RequestMapping(value = "Airplanes/pets", method = RequestMethod.GET)
    /*List<AirplanesPetsDTO> getPetsForAirplanes() {
        List<AirplanesPetsDTO> result = new ArrayList<>();
        for(Airplane Airplane: AirplaneService.getAllAirplanes()) {
            var noPets = 0;
            for(Pet pet: petService.getAllPets()) {
                if (pet.getWid().equals(Airplane.getId())) {
                    noPets += 1;
                }
            }
            result.add(new AirplanesPetsDTO(Airplane.getName(), noPets));
        }
        return result;*/
    //}
}
